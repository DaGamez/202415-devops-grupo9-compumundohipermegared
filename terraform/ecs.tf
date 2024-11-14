resource "aws_ecs_cluster" "app_cluster" {
  name = "cluster-app-python"
}

resource "aws_ecs_task_definition" "app_task" {
  family                   = "python-app-task"
  requires_compatibilities = ["FARGATE"]
  network_mode            = "awsvpc"
  cpu                     = 1024
  memory                  = 3072
  execution_role_arn      = aws_iam_role.ecs_execution_role.arn
  task_role_arn           = aws_iam_role.ecs_task_role.arn

  container_definitions = jsonencode([
    {
      name         = "Container-app-python"
      image        = "${aws_ecr_repository.python_app.repository_url}:latest"
      essential    = true
      environment  = [
        {
          name  = "FLASK_ENV"
          value = "production"
        }
      ]
      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
          protocol      = "tcp"
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/ContainerAppPythonLogs"
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "ContainerAppPythonLogs"
        }
      }
    }
  ])
}

resource "aws_ecs_service" "app_service" {
  name            = "ServiceAppPython"
  cluster         = aws_ecs_cluster.app_cluster.id
  task_definition = aws_ecs_task_definition.app_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = aws_subnet.public[*].id
    security_groups  = [aws_security_group.lb_sg.id]
    assign_public_ip = true
  }

  deployment_controller {
    type = "CODE_DEPLOY"
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.target_group_1.arn
    container_name   = "Container-app-python"
    container_port   = 5000
  }
}
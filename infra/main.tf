module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = var.function_name
  description   = "Lambda responsavel pelo cadastro de usuarios"
  handler       = var.handler
  runtime       = var.runtime
  publish       = true

  create_package         = false
  local_existing_package = "../package.zip"
  depends_on = [ 
    aws_iam_role.lambda_role,
    aws_iam_policy.lambda_policy,
    aws_iam_role_policy_attachment.lambda_attach_policy
  ]

  role_name = aws_iam_role.lambda_role.name
 
}

resource "aws_iam_role" "lambda_role" {
  name = "${var.function_name}_role"

  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action"    : "sts:AssumeRole",
        "Principal" : {
          "Service" : "lambda.amazonaws.com"
        },
        "Effect"    : "Allow",
        "Sid"       : ""
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_policy" {
  name        = "${var.function_name}_policy"
  description = "Policy for Lambda function"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "rds-db:connect"
            ],
            "Resource": "*"
        }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_attach_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}
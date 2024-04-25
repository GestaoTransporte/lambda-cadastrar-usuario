module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = var.function_name
  description   = "Lambda responsavel pelo cadastro de usuarios"
  handler       = var.handler
  runtime       = var.runtime
  publish       = true

  create_package         = false
  local_existing_package = "../package.zip"

}
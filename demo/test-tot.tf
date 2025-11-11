# FILE AN TOAN (DE SO SANH)
resource "aws_security_group" "ssh_an_toan" {
  name = "demo-an-toan"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    # DA SUA: Chi mo cho mang noi bo
    cidr_blocks = ["10.0.0.0/8"]
  }
}

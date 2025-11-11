# KICH BAN 1: FILE VI PHAM
resource "aws_security_group" "ssh_vi_pham" {
  name = "demo-mo-cong-ssh"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    # VI PHAM: Mo cong 22 ra toan the gioi
    cidr_blocks = ["0.0.0.0/0"] 
  }
}

provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "${var.aws_region}"
  version = "1.54.0"
}

data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20200611"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "name-minion" {
  ami             = "${data.aws_ami.ubuntu.id}"
  instance_type   = "t2.micro"
  security_groups = ["salted_server"]
  key_name = "mike_lab"
  tags {
    Name = "name-minion"
  }
}

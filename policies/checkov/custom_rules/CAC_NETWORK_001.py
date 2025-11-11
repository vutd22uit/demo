from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class CACNetwork001Check(BaseResourceCheck):
    def __init__(self):
        name = "Demo: Cam mo cong 22 (SSH) ra 0.0.0.0/0"
        id = "CAC_NETWORK_001"
        supported_resources = ['aws_security_group', 'openstack_networking_secgroup_v2']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        ADMIN_PORTS = [22] # Chi check cong 22 cho demo

        if 'ingress' in conf:
            for ingress_rule in conf['ingress']:
                # Kiem tra xem rule co cho phep 0.0.0.0/0 khong
                if self.is_overly_permissive(ingress_rule):
                    # Kiem tra xem cong co nam trong danh sach cam khong
                    port = self.get_port(ingress_rule)
                    if port in ADMIN_PORTS:
                        return CheckResult.FAILED # Vi pham
        
        return CheckResult.PASSED # An toan

    def is_overly_permissive(self, rule):
        """Kiem tra xem rule co cidr_blocks chua '0.0.0.0/0' khong."""
        cidr_blocks = rule.get('cidr_blocks', [[]])
        if not cidr_blocks or not cidr_blocks[0]:
            return False
        return '0.0.0.0/0' in cidr_blocks[0]

    def get_port(self, rule):
        """Trich xuat cong tu rule."""
        from_port = rule.get('from_port', [None])[0]
        to_port = rule.get('to_port', [None])[0]
        return from_port if from_port else to_port

# Dang ky rule nay voi Checkov
scanner = CACNetwork001Check()

import os
import time

def create_playbook(image_name: str, blades: list):

    content = f"""
- name: Provision Testbed
  hosts: all
  become: yes

  tasks:
    - name: Print selected image
      debug:
        msg: "Deploying {image_name}"

    - name: Simulate blade provisioning
      debug:
        msg: "Configuring blade {{item}}"
      loop: {blades}
"""

    filename = f"playbooks/provision_{int(time.time())}.yml"

    os.makedirs("playbooks", exist_ok=True)

    with open(filename, "w") as f:
        f.write(content)

    return filename
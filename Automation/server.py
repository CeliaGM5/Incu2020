#CELIA GOMEZ MEGIAS
import socket
import ncclient
from ncclient import manager
from ncclient.operations import TimeoutExpiredError
import xml.dom.minidom
import pprint



def nexus_version_query(request):
        try:
                device_connection = ncclient.manager.connect(
                        host='127.0.0.1',
                        port=2222,
                        username='admin',
                        password='Cisco!123',
                        hostkey_verify=False,
                        device_params={'name': 'nexus'},
                        allow_agent=False,
                        look_for_keys=False
                )
                print("Connected to the device!")
        except:
                print("Failure...")
        int_filter = '''
                               <show xmlns="http://www.cisco.com/nxos:1.0">
                                     <version></version>
                               </show>
                   '''
        netconf_output = device_connection.get(('subtree', int_filter))

        return netconf_output

def get_version(response):
        xml_doc = xml.dom.minidom.parseString(response.xml)
        nxos_ver_str = xml_doc.getElementsByTagName("mod:nxos_ver_str")
        version = (nxos_ver_str[0].firstChild.nodeValue)
        return version

def nexus_change_hostname(new_hostname):
        import ncclient
        from ncclient import manager
        from ncclient.operations import TimeoutExpiredError
        import xml.dom.minidom
        try:
                device_connection = ncclient.manager.connect(
                        host='127.0.0.1',
                        port=2222,
                        username='admin',
                        password='Cisco!123',
                        hostkey_verify=False,
                        device_params={'name': 'nexus'},
                        allow_agent=False,
                        look_for_keys=False
                )
                print("Connected to the device!")
        except:
                print("Failure...")

        name = new_hostname
        new_config = '''
            <config>
                               <configure xmlns="http://www.cisco.com/nxos:1.0">
                                     <__XML__MODE__exec_configure>
                                             <hostname><name>%s</name></hostname>
                                     </__XML__MODE__exec_configure>
                               </configure>
            </config>
                   '''
        configuration = new_config % name
        device_connection.edit_config(target='running', config=configuration)

        print("Config pushed successfuly!")


def Main():

        host = "127.0.0.1"
        port = 5000
        s_version="show version"

        mySocket = socket.socket()
        mySocket.bind((host, port))

        mySocket.listen(5)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        while True:
                message = conn.recv(1024).decode()
                if message == s_version:
                        try:
                                response = nexus_version_query(message)
                                version = get_version(response)
                                message = "Version " + version
                        except:
                                print("Unable to get this node version")
                elif message.startswith("hostname", 0):
                        try:
                                name = message[9:]
                                nexus_change_hostname(name)
                                message = "Hostname changed to " + name
                        except:
                                print("Unable to change this node hostname")
                else:
                        message = "Try it again. I don't understand."

                conn.send(message.encode())
        conn.close()

if __name__ == '__main__':
        Main()





# PenetrationTesting                                                                                                                                                             


**COMPANY**: CODTECH IT SOLUTIONS                                                                                                                                                 

**NAME**: GOGULA SUSMITHA                                                                                                                                                         

**INTERN ID**: CT12WKPH                                                                                                                                                           

**DOMAIN**: CYBER SECURITY & ETHICAL HACKING                                                                                                                                      

**BATCH DURATION**: January 10th, 2025 to April 10th, 2025                                                                                                                       

**MENTOR**: Neela Santhosh Kumar  

**DESCRIPTION**:                                                                                                                                                                 
        The primary objective of this task is to design and implement a modular penetration testing toolkit using the Python programming language. This toolkit will comprise several independent modules, each dedicated to performing a specific penetration testing function. The initial scope of the toolkit will include at least two essential modules: a port scanner and a brute-force attack tool. The toolkit should be structured in a way that allows for easy expansion with additional modules in the future, promoting flexibility and adaptability for various security assessment needs. A crucial aspect of this deliverable is comprehensive documentation that clearly explains the purpose, functionality, usage, and any dependencies of each module within the toolkit.

The modular design is central to this task. Each module should function as a self-contained unit, encapsulating the logic and resources required for its specific task. This approach offers several advantages, including improved code organization, easier debugging and maintenance, and the ability to integrate new functionalities without significantly impacting existing modules.

The first module to be developed is a Port Scanner. This module will be responsible for identifying open ports on a target host or a range of hosts. Port scanning is a fundamental technique in penetration testing and network reconnaissance. It allows security professionals to determine which services are running on a target system, as each network service typically listens on a specific port number. The port scanner module should:                                                                                  
**1.** Accept a target IP address or hostname as input.                                                                                                                       

**2.** Allow the user to specify a range of ports to scan (e.g., common ports, all ports, or a custom range).                                                                 

**3.** Utilize Python's networking capabilities (likely through the socket module) to attempt to establish a connection with each specified port on the target host.          

**4.** Determine whether a port is open (accepting connections), closed (rejecting connections), or filtered (no response, possibly due to a firewall).                       

**5.** Present the scan results to the user in a clear and informative manner, indicating the status of each scanned port.                                                    

The second module to be developed is a Brute-Force Attack Tool. This module will aim to gain unauthorized access to a target service by systematically trying a large number of potential usernames and passwords. Brute-force attacks are often used against authentication mechanisms such as SSH, FTP, or web login forms. The brute-forcer module should:                                                                                                                                                                       

**1.** Allow the user to specify the target service (e.g., SSH, FTP, HTTP).                                                                                                   

**2.** Accept the target host and port number as input.                                                                                                                       

**3.** Enable the user to provide lists of usernames and passwords (either as command-line arguments or through file paths).                                                  

**4.** Implement the logic to attempt authentication with the target service using each combination of username and password from the provided lists. This will likely involve using appropriate Python libraries for interacting with the specified service (e.g., paramiko for SSH, ftplib for FTP, requests for HTTP forms).                      

**5.** Report successful login attempts, if any, including the username and password that worked.                                                                             

**6.** Include options to control the rate of attempts to avoid account lockout or overwhelming the target service.                                                           

**OUTPUT**: <img width="718" alt="Image" src="https://github.com/user-attachments/assets/6a5348fb-03d3-4e0e-945d-48b097a5cc6b" />

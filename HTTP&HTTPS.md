# 1. What is HTTP?  
HTTP (Hypertext Transfer Protocol) 
HTTP is the foundation of data communication on the World Wide Web. It allows web browsers and servers to communicate with each other by transmitting hypertext (text, images, videos, etc.). HTTP operates at the application layer in the OSI model and uses a request-response model to transfer information between a client (typically a web browser) and a server.

**How HTTP works:**

**Client Request:** The client sends an HTTP request (usually by typing a URL in a browser or clicking a link).  
**Server Response:** The server processes the request and sends back the appropriate HTTP response containing the requested resources (e.g., HTML page, image, etc.).

**Example:**

GET /index.html HTTP/1.1  
Host: www.example.com

# Drawback of HTTP  
The primary issue with HTTP is that it is not secure. All communication between the client and the server is sent in plain text, making it vulnerable to interception and attacks such as Man-in-the-Middle (MitM), where attackers can eavesdrop or even alter the data.

# 2. What is HTTPS?  
HTTPS (Hypertext Transfer Protocol Secure)  
HTTPS is the secure version of HTTP. It adds a layer of encryption using SSL (Secure Sockets Layer) or TLS (Transport Layer Security) to secure the data transmitted between the client and the server. This encryption ensures that even if a third party intercepts the data, they will not be able to read it without the encryption key.

**How HTTPS works:**

- **Client-Server Handshake:** Before any actual data is sent, the client and server perform a “handshake” to agree on the encryption protocols and exchange keys.  
- **Data Encryption:** After the handshake, the data transmitted between the client and the server is encrypted using SSL/TLS, ensuring confidentiality and integrity.  
- **Certificate Verification:** HTTPS also uses digital certificates (issued by a trusted Certificate Authority — CA) to verify the server’s authenticity, preventing phishing attacks where users are tricked into communicating with a fake server.  

**Example:** When visiting https://www.example.com, your browser checks the server’s SSL certificate and establishes a secure connection before transmitting any data.

# How HTTPS Makes Things Secure:  

- **Encryption:** Encrypts data so it is not readable during transmission.  
- **Data Integrity:** Ensures the data is not altered during transfer.  
- **Authentication:** Verifies the identity of the website, preventing attacks like impersonation.

https://devcookies.medium.com/http-vs-https-and-ssl-how-it-works-and-why-it-matters-86ae9e1d51c3

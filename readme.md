
# Engineering Requirements Specification Component

>FalaSó is a chatbot project led by a small development team for a telecommunications company. Its core purpose is to provide AI-driven technical support through an accessible web application. This initiative aims to decrease the reliance on human tech support agents by offering quick answers, knowledge-based troubleshooting, and assistance with ticket creation or scheduling on-site help.

# FalaSó
FalaSó is an AI-powered chatbot being developed by a small team of developers for a telecommunications company. The chatbot aims to assist users needing technical support through a web application, reducing the number of requests for human technical support.

The chatbot's primary functions include answering general questions and providing knowledge-based solutions to common technical issues. It can also help create detailed support tickets and schedule on-site assistance, thereby simplifying the support process and improving user experience.

Users will interact with the Bot via chat available in a webapp. The support functionalities each user has access to are dependent on authentication. Authentication ensures appropriate handling of sensitive technical support tasks that involve personal or private information.

The application is designed with an adaptive approach to ensure intuitive navigation and seamless  integration across various devices (desktop, tablet, smartphone), enabling compatibility with existing customer support workflows.

# 1. Actors and User Stories

In this section you can find detailed actor specifications and their corresponding user stories.

## 1.1 Actors

Diagram identifying actors and their relationships.

![Actors diagram](docs\fala-so_actors_diagram.png)

| Identifier           | Description |
|----------------------|-------------|
| **Guest**           | An unauthenticated user who can interact with the chatbot for basic functionalities that do not require access to sensitive or private information. |
| **Authenticated User** | A logged-in user who has access to chatbot features that involve private customer data, such as account-specific support or service management. |
| **Technical Support** | A support agent who has access to support tickets that require further assistance beyond what the chatbot can resolve. They can view, update, and manage escalated cases. |

## 1.2 User Stories

In this section you can find the user stories for our system. Both Authenticated Users and Admins can also do Guests' actions.

### 1.2.1 Guest

| Identifier | Name | Priority | Description |
| ----------- | ----------- | ----------- | ----------- |
| **US.100** | Sign-in | High | As a guest, I would like to sign-in to my account, so that i can have access to account-specific support or service management. |
| **US.101** | New Phone Number | High | As a guest, I want to be able to request a new phone number and be contacted afterward so that I can set up a new phone service. |
| **US.102** | Text | Title | Title |
| **US.103** | Text | Title | Title |
| **US.104** | Text | Title | Title |
| **US.105** | Text | Title | Title |
| **US.106** | Text | Title | Title |

Comments:
	These will be heavily dependent on the script provided by the company.

### 1.2.2 Authenticated User
| Identifier | Name | Priority | Description |
| ----------- | ----------- | ----------- | ----------- |
| **US.200** | Phone Number Support | Medium | As an authenticated user, I want to specify the phone number for which I need technical support so that I can receive assistance for the correct number. |
| **US.201** | Text | Title | Title |
| **US.202** | Text | Title | Title |

Comments:
	As authenticated user should i have acces to to previous chats and tickets?

### 1.2.3 Technical Support
| Identifier | Name | Priority | Description |
| ----------- | ----------- | ----------- | ----------- |
| **US.300** | View Tickets | High | As a technical support agent, I want to view all open tickets so that I can prioritize and address them accordingly. |
| **US.301** | Detailed Tickets | High | As a technical support agent, I want each support ticket to include comprehensive details about the issue so that I can efficiently diagnose and resolve it. |

## 2 Supplementary Requirements

This section contains business rules, technical requirements and other non-functional requirements on the project.

### 2.1 Business Rules

A business rule provides explicit guidance or restrictions for actions, decisions, and processes in an organization, aiming to establish uniformity, compliance, and efficiency.

| Identifier | Name | Description |
| ----------- | ----------- | ----------- |
| **BR.100** | User Authentication | All users must authenticate before accessing account-specific support, service management, or any features involving private customer data. |
| **BR.101** | Support Tickets Limit | Users are restricted to a predefined number of support requests within a specific time frame. |
| **BR.102** | Relevant Queries Only | The chatbot is limited to answering questions strictly related to the designated subject matter to maintain accuracy and relevance. |

### 2.2 Technical Requirements  

Technical requirements define the essential features and conditions a system must meet. They serve as a foundation for the development, evaluation, and maintenance of the product’s **performance, security, scalability, and usability**.  

| **Identifier** | **Name** | **Description** |
|--------------|---------|---------------------------|
| **TR.100** | Security | The system must implement authentication, encryption, and role-based access control (RBAC) to protect customer data. It must also include safeguards against DDoS, Man-in-the-Middle (MitM), and other cyber threats. |
| **TR.101** | Robustness | The system must be resilient and capable of handling errors without failure, ensuring continuous operation. |
| **TR.102** | Scalability | The system must be designed to accommodate increasing user loads and interactions while maintaining smooth performance. |
| **TR.103** | Database Access | Authenticated users must have secure access to the company’s database to enable personalized customer service. |
| **TR.104** | Usability | The user interface must be simple and intuitive, catering to users of all ages and technical backgrounds. |
| **TR.105** | Performance | The system must maintain **low latency** and **fast response times**, ensuring an optimal user experience even under high demand. |
| **TR.106** | Web Application | The system must be developed as a **web application** using standard web technologies (HTML, JavaScript, CSS, and PHP). |

### 2.3 Restrictions

A restriction outlines a limitation or constraint that the system or project must adhere to. It helps define boundaries and guide decision-making during development and use.

## 3 Information Architecture

This artifact presents an overview of the information architecture of FalaSó. It offers a preview of the web app's user interface and demonstrates in a quick and simple manner how the system is organized.

It comprises two components:

* A sitemap outlining the organization of information across pages;
* A wireframe delineating the functionality and content for homepage.

### 3.1 Sitemap



### 3.2 Wireframe

![Wireframe](docs\fala-so_sitemap_diagram.png)




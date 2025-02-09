
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

![Actors diagram](docs\fala-so_actors_diagram.drawio.png)

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

## 1.3 Supplementary Requirements

This section contains business rules, technical requirements and other non-functional requirements on the project.

### 1.3.1 Business Rules

A business rule provides explicit guidance or restrictions for actions, decisions, and processes in an organization, aiming to establish uniformity, compliance, and efficiency.

| Identifier | Name | Description |
| ----------- | ----------- | ----------- |
| **BR.100** | User Authentication | All users must authenticate before accessing account-specific support or service management. |

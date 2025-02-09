
# Engineering Requirements Specification Component

FalaSó is a chatbot project led by a small development team for a telecommunications company. Its core purpose is to provide AI-driven technical support through an accessible web application. This initiative aims to decrease the reliance on human tech support agents by offering quick answers, knowledge-based troubleshooting, and assistance with ticket creation or scheduling on-site help.

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
| **US.100** | Title | Title | Title |
| **US.101** | Text | Title | Title |

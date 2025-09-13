# Cat Facts API

**Cat Facts API** is a RESTful web service built with **FastAPI** that allows users to fetch, store, and manage cat facts. This project demonstrates integration with a 3rd-party API, CRUD operations, caching, rate-limiting, and API key authentication.

---

## Table of Contents

1. [Project Description](#project-description)  
2. [Installation](#installation)  
3. [Running the Server](#running-the-server)  
4. [API Endpoints](#api-endpoints)  
5. [Advanced Features](#advanced-features)  
6. [Screenshots](#screenshots)  
7. [Notes](#notes)  

---

## Project Description

This project:

- Fetches cat facts from [`catfact.ninja`](https://catfact.ninja/)  
- Stores cat facts in a local SQLite database via SQLAlchemy  
- Supports CRUD operations (Create, Read, Update, Delete)  
- Implements rate limiting to prevent abuse (5 requests per minute per IP)  
- Implements caching with FastAPI Cache (responses cached for 60 seconds)  
- Secures certain endpoints with API key authentication  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/JPretz/sweng861-2025-FALL-cats-api.git
cd sweng861-2025-FALL-cats-api/Backend/catfacts_bonus

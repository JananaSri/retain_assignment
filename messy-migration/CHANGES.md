# CHANGES.md

## Major Issues Identified
1. All code was in a single file — hard to maintain.
2. No password hashing — stored plain text passwords.
3. No input validation — allowed empty/invalid fields.
4. Inconsistent HTTP status codes.
5. No clear error handling.

## Changes Made
1. Split project into routes, models, services, utils.
2. Added password hashing with werkzeug.security.
3. Implemented input validation for required fields.
4. Standardized HTTP status codes.
5. Added minimal tests for key functionality.

## Trade-offs
- Used simple manual validation instead of Pydantic to save time.
- Kept SQLite for simplicity instead of PostgreSQL.

## With More Time
- Add JWT-based authentication.
- Add pagination for GET /users.
- Implement more comprehensive tests.

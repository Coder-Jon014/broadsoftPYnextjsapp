# Broadworks OCIP API Interface

## Description
This project provides a web-based interface for interacting with the Broadworks OCIP API. It allows users to fetch and display various types of data including call logs, user login information, and detailed user information.

## Features
- Fetch and display user call logs (missed and received calls)
- Retrieve and show user login information
- Get detailed user information
- User-friendly web interface for easy data access

## Technologies Used
- Backend:
  - Flask (Python)
  - Broadworks OCIP API
- Frontend:
  - Next.js (React)
  - TypeScript
  - Tailwind CSS
  - shadcn/ui components

## Prerequisites
- Python 3.7+
- Node.js 14+
- npm or yarn
- Broadworks OCIP API credentials

## Installation

### Backend Setup
1. Clone the repository:
   ```
   git clone https://github.com/your-username/broadworks-ocip-interface.git
   cd broadworks-ocip-interface
   ```

2. Set up a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Broadworks OCIP API credentials:
   ```
   API_HOST=your_api_host
   API_PORT=your_api_port
   API_USERNAME=your_username
   API_PASSWORD=your_password
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

## Running the Application

1. Start the Flask backend server:
   ```
   python app.py
   ```

2. In a new terminal, start the Next.js frontend:
   ```
   cd frontend
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:3000` to use the application.

## Usage
1. Select the desired function from the dropdown menu:
   - Call Logs
   - User Login Info
   - User Details
2. Enter the User ID in the input field.
3. Click "Fetch Data" to retrieve and display the information.

## API Endpoints
- `/call-logs`: Fetches user call logs
- `/user-login-info`: Retrieves user login information
- `/user-get`: Gets detailed user information

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
[MIT License](LICENSE)

## Acknowledgements
- Broadworks OCIP API documentation
- Flask documentation
- Next.js documentation
- shadcn/ui component library
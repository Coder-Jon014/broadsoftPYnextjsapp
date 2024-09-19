'use client';
import { useState, useEffect } from 'react';
import CallLogs from '@/components/CallLogs';
import UserLoginInfo from '@/components/UserLoginInfo';
import UserGetInfo from '@/components/UserGetInfo';

export default function Home() {
  const [userId, setUserId] = useState('');
  const [selectedFunction, setSelectedFunction] = useState('UserBasicCallLogsGetListRequest');
  const [result, setResult] = useState<any>(null);

  // Reset the result when function changes
  useEffect(() => {
    setResult(null);
  }, [selectedFunction]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    let apiUrl = '';
    if (selectedFunction === 'UserBasicCallLogsGetListRequest') {
      apiUrl = `/api/call-logs?function=${selectedFunction}&user_id=${userId}`;
    } else if (selectedFunction === 'UserGetLoginInfoRequest') {
      apiUrl = `/api/user-login-info?function=${selectedFunction}&user_id=${userId}`;
    } else if (selectedFunction === 'UserGetRequest22') {
      apiUrl = `/api/user-get?function=${selectedFunction}&user_id=${userId}`;
    }

    try {
      const res = await fetch(apiUrl);
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      const data = await res.json();
      setResult(data);
    } catch (error) {
      console.error('Error fetching data:', error);
      setResult({ error: 'Failed to fetch data' });
    }
  };

  const renderResult = () => {
    if (!result) return null;

    if (result.error) {
      return <div className="text-red-500">{result.error}</div>;
    }

    if (selectedFunction === 'UserBasicCallLogsGetListRequest' && result.missed_calls && result.received_calls) {
      return (
        <CallLogs 
          missedCalls={result.missed_calls} 
          receivedCalls={result.received_calls} 
        />
      );
    } else if (selectedFunction === 'UserGetLoginInfoRequest') {
      return <UserLoginInfo loginInfo={result} />;
    } else if (selectedFunction === 'UserGetRequest22') {
      return <UserGetInfo userInfo={result} />;
    }

    return null;
  };

  return (
    <div className="container mx-auto max-w-4xl p-4 flex flex-col h-screen">
      <h1 className="text-3xl font-bold mb-6 text-center">API Data Fetcher</h1>
      
      <form onSubmit={handleSubmit} className="mb-8">
        <div className="flex flex-col space-y-4">
          <div>
            <label htmlFor="function" className="block mb-2">Select Function:</label>
            <select 
              id="function" 
              value={selectedFunction} 
              onChange={(e) => setSelectedFunction(e.target.value)}
              className="w-full p-2 border rounded"
            >
              <option value="UserBasicCallLogsGetListRequest">Call Logs</option>
              <option value="UserGetLoginInfoRequest">User Login Info</option>
              <option value="UserGetRequest22">User Details</option>
            </select>
          </div>

          <div>
            <label htmlFor="user_id" className="block mb-2">User ID:</label>
            <input
              type="text"
              id="user_id"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              required
              className="w-full p-2 border rounded"
            />
          </div>

          <button type="submit" className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
            Fetch Data
          </button>
        </div>
      </form>

      <div className="flex-grow overflow-auto">
        {renderResult()}
      </div>
    </div>
  );
}

'use client';
import { useState } from 'react';
import CallLogs from '@/components/CallLogs';

export default function Home() {
  const [userId, setUserId] = useState('');
  const [selectedFunction, setSelectedFunction] = useState('UserBasicCallLogsGetListRequest');
  const [result, setResult] = useState<any>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    let apiUrl = '';
    if (selectedFunction === 'UserBasicCallLogsGetListRequest') {
      apiUrl = `/api/call-logs?function=${selectedFunction}&user_id=${userId}`;
    } else if (selectedFunction === 'UserGetLoginInfoRequest') {
      apiUrl = `/api/user-login-info?function=${selectedFunction}&user_id=${userId}`;
    }

    const res = await fetch(apiUrl);
    const data = await res.json();
    setResult(data);
  };

  const renderResult = () => {
    if (!result) return null;

    if (selectedFunction === 'UserBasicCallLogsGetListRequest') {
      return (
        <CallLogs 
          missedCalls={result.missed_calls} 
          receivedCalls={result.received_calls} 
        />
      );
    } else if (selectedFunction === 'UserGetLoginInfoRequest') {
      return (
        <ul>
          {Object.entries(result).map(([key, value]) => (
            <li key={key}>{key}: {value !== null ? String(value) : 'None'}</li>
          ))}
        </ul>
      );
    }
  };

  return (
    <div>
      <h1>API Data Fetcher</h1>
      
      <form onSubmit={handleSubmit}>
        <label htmlFor="function">Select Function:</label>
        <select id="function" value={selectedFunction} onChange={(e) => setSelectedFunction(e.target.value)}>
          <option value="UserBasicCallLogsGetListRequest">Call Logs</option>
          <option value="UserGetLoginInfoRequest">User Login Info</option>
        </select>

        <label htmlFor="user_id">User ID:</label>
        <input
          type="text"
          id="user_id"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />

        <button type="submit">Fetch Data</button>
      </form>

      <div>
        <h2>Result</h2>
        {renderResult()}
      </div>
    </div>
  );
}

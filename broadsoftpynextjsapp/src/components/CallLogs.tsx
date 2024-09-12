// src/components/CallLogs.tsx
interface CallLog {
    name: string;
    phone_number: string;
    time: string;
  }
  
  interface CallLogsProps {
    missedCalls: CallLog[];
    receivedCalls: CallLog[];
  }
  
  export default function CallLogs({ missedCalls, receivedCalls }: CallLogsProps) {
    return (
      <div>
        <h3>Missed Calls</h3>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Phone Number</th>
              <th>Time</th>
            </tr>
          </thead>
          <tbody>
            {missedCalls.map((call, index) => (
              <tr key={index}>
                <td>{call.name}</td>
                <td>{call.phone_number}</td>
                <td>{new Date(call.time).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
  
        <h3>Received Calls</h3>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Phone Number</th>
              <th>Time</th>
            </tr>
          </thead>
          <tbody>
            {receivedCalls.map((call, index) => (
              <tr key={index}>
                <td>{call.name}</td>
                <td>{call.phone_number}</td>
                <td>{new Date(call.time).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
  
"use client"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

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
  const renderCallTable = (calls: CallLog[], title: string) => (
    <div className="mb-8">
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>Phone Number</TableHead>
            <TableHead>Time</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {calls.map((call, index) => (
            <TableRow key={index}>
              <TableCell>{call.name}</TableCell>
              <TableCell>{call.phone_number}</TableCell>
              <TableCell>{new Date(call.time).toLocaleString()}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );

  return (
    <>
      <h2 className="text-2xl font-bold mb-4 text-center">Call Logs</h2>
      {renderCallTable(missedCalls, "Missed Calls")}
      {renderCallTable(receivedCalls, "Received Calls")}
    </>
  );
}

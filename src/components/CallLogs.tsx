"use client"

import {
  Table,
  TableBody,
  TableCaption,
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
  const renderCallTable = (calls: CallLog[], caption: string) => (
    <Table>
      <TableCaption>{caption}</TableCaption>
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
  );

  return (
    <div>
      {renderCallTable(missedCalls, "Missed Calls")}
      {renderCallTable(receivedCalls, "Received Calls")}
    </div>
  );
}

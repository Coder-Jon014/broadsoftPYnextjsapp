import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface UserLoginInfoProps {
  loginInfo: {
    "User ID": string | null;
    "First Name": string | null;
    "Last Name": string | null;
    "Group ID": string | null;
  };
}

export default function UserLoginInfo({ loginInfo }: UserLoginInfoProps) {
  return (
    <>
      <h2 className="text-2xl font-bold mb-4 text-center">User Login Information</h2>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>User ID</TableHead>
            <TableHead>First Name</TableHead>
            <TableHead>Last Name</TableHead>
            <TableHead>Group ID</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow>
            <TableCell>{loginInfo["User ID"] || 'None'}</TableCell>
            <TableCell>{loginInfo["First Name"] || 'None'}</TableCell>
            <TableCell>{loginInfo["Last Name"] || 'None'}</TableCell>
            <TableCell>{loginInfo["Group ID"] || 'None'}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </>
  );
}

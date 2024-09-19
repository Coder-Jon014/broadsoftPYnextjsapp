import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface UserLoginInfoProps {
  loginInfo: Record<string, string | null>;
}

export default function UserLoginInfo({ loginInfo }: UserLoginInfoProps) {
  return (
    <>
      <h2 className="text-2xl font-bold mb-4 text-center">User Login Information</h2>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Attribute</TableHead>
            <TableHead>Value</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {Object.entries(loginInfo).map(([key, value]) => (
            <TableRow key={key}>
              <TableCell className="font-medium">{key}</TableCell>
              <TableCell>{value !== null ? value : 'None'}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </>
  );
}

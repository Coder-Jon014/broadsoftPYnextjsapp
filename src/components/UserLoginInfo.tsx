import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface UserLoginInfoProps {
  loginInfo: Record<string, any>;
}

export default function UserLoginInfo({ loginInfo }: UserLoginInfoProps) {
  return (
    <Table>
      <TableCaption>User Login Information</TableCaption>
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
            <TableCell>{value !== null ? String(value) : 'None'}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

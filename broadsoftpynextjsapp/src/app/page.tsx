// src/app/page.tsx
export default async function Home() {
  const res = await fetch('http://localhost:3000/api/hello');
  const data = await res.json();

  return <div>{data.message}</div>;
}

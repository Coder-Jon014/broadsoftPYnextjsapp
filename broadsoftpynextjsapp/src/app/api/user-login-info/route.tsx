// src/app/api/user-login-info/route.ts
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const userId = searchParams.get('user_id');

  const res = await fetch(`http://localhost:5000/user-login-info?user_id=${userId}`);
  const data = await res.json();

  return NextResponse.json(data);
}

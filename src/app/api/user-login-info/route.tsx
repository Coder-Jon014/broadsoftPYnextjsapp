// src/app/api/user-login-info/route.ts
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const func = searchParams.get('function');
  const userId = searchParams.get('user_id');

  let apiUrl = 'http://localhost:5000';
  if (func === 'UserLoginInfoGetRequest') {
    apiUrl += `/user-login-info?user_id=${userId}`;
  }
  const res = await fetch(apiUrl);
  const data = await res.json();

  return NextResponse.json(data);
}

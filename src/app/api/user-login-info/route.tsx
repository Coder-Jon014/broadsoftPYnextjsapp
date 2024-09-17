// src/app/api/user-login-info/route.ts
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const func = searchParams.get('function');
  const userId = searchParams.get('user_id');

  let apiUrl = 'http://localhost:5000';
  if (func === 'UserGetLoginInfoRequest') {
    apiUrl += `/user-login-info?user_id=${userId}`;
  }

  try {
    const res = await fetch(apiUrl);
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    const data = await res.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error fetching user login info:', error);
    return NextResponse.json({ error: 'Failed to fetch user login info' }, { status: 500 });
  }
}

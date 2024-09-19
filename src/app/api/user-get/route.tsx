import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const func = searchParams.get('function');
  const userId = searchParams.get('user_id');

  let apiUrl = 'http://localhost:5000';
  if (func === 'UserGetRequest22') {
    apiUrl += `/user-get?user_id=${userId}`;
  }

  try {
    const res = await fetch(apiUrl);
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    const data = await res.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error fetching user details:', error);
    return NextResponse.json({ error: 'Failed to fetch user details' }, { status: 500 });
  }
}

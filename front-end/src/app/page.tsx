'use client'
import React, { useEffect, useState } from 'react'

function Page() {
  const [message, setMessage] = useState("Loading");
  const [people, setPeople] = useState(['Waiting'])

  useEffect(()=>{
    fetch("http://localhost:8080/home")
    .then((response)=>response.json())
    .then((data)=>{
      setMessage(data.message)
      setPeople(data.people)
    })
  }, [])


  return (
    <div>{message}
    <div>Special thanks to {people}</div>
    </div>
  )
}

export default Page
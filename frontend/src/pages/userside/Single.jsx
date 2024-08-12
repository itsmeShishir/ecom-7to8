import {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom';

const Single = () => {
    const {id} = useParams();
    const [singledata, Setsingeldata] = useState({});

    useEffect(()=>{
        const fetchdata = async()=>{
            try{
            let res =  await fetch(`http://127.0.0.1:8000/singleProduct/${id}`)
            let datas = await res.json();
            Setsingeldata(datas)
            console.log(datas)
            }catch(e){
                console.log(e.message)
            }
        }
        fetchdata()
    },[])
  return (
    <div>
        <h1>{singledata.title}</h1>
        <img src={singledata.img} alt={singledata.title} />
        <p>{singledata.description}</p>
        <p>Price: {singledata.price}</p>
        <button>GO BACK TO HOME</button>
    </div>
  )
}

export default Single

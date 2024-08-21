import { useState } from "react";
import axios from "axios";

const AddCategory = () => {
  const [data, setData] = useState({
    title: "",
    username: "",
    img: null, 
    description: ""
  });

  function handleChange(event) {
    const { name, value } = event.target;
    if (name === "img") {
      setData((items) => ({
        ...items,
        img: event.target.files[0],  
      }));
    } else {
      setData((items) => ({
        ...items,
        [name]: value,
      }));
    }
  }

  const onSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("title", data.title);
    formData.append("description", data.description);
    formData.append("img", data.img);
    formData.append("username", data.username);

    try {
      await axios.post("http://127.0.0.1:8000/addCategory/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",  
        },
      });
      console.log("Category added successfully");
    } catch (err) {
      console.log("Category creation failed", err);
    }
  };

  return (
    <>
      <form onSubmit={onSubmit}>
        <div className="flex flex-col justify-center max-w-lg mx-auto px-4 space-y-6 font-[sans-serif] text-[#333]">
          <div>
            <label className="mb-2 text-lg block">Title</label>
            <input
              type="text"
              name="title"
              value={data.title}
              onChange={handleChange}
              placeholder="Large Input"
              className="px-4 py-2.5 text-lg rounded-md bg-white border border-gray-400 w-full outline-blue-500"
            />
          </div>
          <div>
            <label className="mb-2 text-lg block">Description</label>
            <input
              type="text"
              name="description"
              value={data.description}
              onChange={handleChange}
              placeholder="Large Input"
              className="px-4 py-2.5 text-lg rounded-md bg-white border border-gray-400 w-full outline-blue-500"
            />
          </div>
          <div className="font-[sans-serif] max-w-md mx-auto">
            <label className="text-base text-gray-500 font-semibold mb-2 block">Upload file</label>
            <input
              type="file"
              name="img"
              onChange={handleChange}
              className="w-full text-gray-400 font-semibold text-sm bg-white border file:cursor-pointer cursor-pointer file:border-0 file:py-3 file:px-4 file:mr-4 file:bg-gray-100 file:hover:bg-gray-200 file:text-gray-500 rounded"
            />
            <p className="text-xs text-gray-400 mt-2">
              PNG, JPG SVG, WEBP, and GIF are Allowed.
            </p>
          </div>
          <div>
            <label className="mb-2 text-lg block">User</label>
            <input
              type="text"
              name="username"
              value={data.username}
              onChange={handleChange}
              placeholder="Large Input"
              className="px-4 py-2.5 text-lg rounded-md bg-white border border-gray-400 w-full outline-blue-500"
            />
          </div>
          <button
            type="submit"
            className="px-5 py-2.5 rounded-lg text-white text-sm tracking-wider font-medium border border-current outline-none bg-blue-700 hover:bg-blue-800 active:bg-blue-700"
          >
            Submit
          </button>
        </div>
      </form>
    </>
  );
};

export default AddCategory;

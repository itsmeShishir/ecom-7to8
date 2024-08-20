import { Outlet } from "react-router-dom"
import SideBar from "./sidebar"

const Dashboard = () => {
  return (
    <div>
      <div>
        <SideBar />
        <div>
          <h1> Admin Dashboard</h1>
      <Outlet />
        </div>
      </div>
        
    </div>
  )
}

export default Dashboard

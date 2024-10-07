// Import essential React stuff
import axios from 'axios'
import React, { useContext, useEffect, useState } from 'react'
import ReactDOM from 'react-dom/client'

// Import defaults and context
import addonData from '/src/common'
import { AddonProvider, AddonContext } from '@ynput/ayon-react-addon-provider'
import '@ynput/ayon-react-components/dist/style.css'

// Import your App
import App from './App.jsx'


function Index() {
  const context = useContext(AddonContext)

  const [tokenSet, setTokenSet] = useState(false)


  useEffect(() => {
    if (addonName && addonVersion) {
      addonData.addonName = addonName;
      addonData.addonVersion = addonVersion;
      addonData.baseUrl = `${window.location.origin}/api/addons/${addonName}/${addonVersion}`;
      console.log("BaseUrl", addonData.baseUrl);
    }
  }, [addonName, addonVersion]);

  useEffect(() => {
    if (accessToken && !tokenSet) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`
      setTokenSet(true)
    }
  }, [accessToken, tokenSet])

  if (!context) {
    return <p>Loading...</p>
  }

  const accessToken = context.accessToken
  const addonName = context.addonName
  const addonVersion = context.addonVersion



  if (!tokenSet) {
    return <p>No token found!</p>
  }

  return <App />
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <AddonProvider>
      <Index />
    </AddonProvider>
  </React.StrictMode>,
)
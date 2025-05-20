import React, { useState } from "react";

const Tabs = ({tabs }) => {
    const [activeTab, setActiveTab] = useState(0);

    return (
        <div className="tabs">
            <div className="tab-headers">
                {tabs.map((tab, index) => (
                    <button
                        key={index}
                        className={`tab-button ${activeTab === index ? "active" : ""}`}
                        onClick={() => setActiveTab(index)}
                    >
                    {tab.label}
                    </button>
                ))}
            </div>
            <div className="tab-content">{tabs[activeTab].content}</div>
        </div> 
    );
};

export default Tabs;
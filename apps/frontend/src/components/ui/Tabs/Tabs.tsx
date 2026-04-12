import { useState } from "react";

export default function Tabs(tabs) {
    // state
    const [activeTab, setActiveTab] = useState<number>(0);

    return (
        <div className="tab">
            <div className="tab-headers">
                { tabs.map((tab, index) => (
                    <button
                        key={index}
                        onClick={() => setActiveTab(index)}
                    >
                        { tab.label }
                    </button>
                ))}
            </div>
            <div className="tab-content">
                <div>{ tabs[activeTab].content }</div>
            </div>
        </div>
    );
}
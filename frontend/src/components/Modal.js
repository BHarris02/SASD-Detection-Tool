import React from "react";
import PropTypes from "prop-types";

const Modal = ({ show, onClose, title, children }) => {
    if (!show) return null;

    return (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <h3>{title}</h3>
              <button onClick={onClose} className="close-modal">Close</button>
            </div>
            <div className="modal-body">
              {children}
            </div>
          </div>
        </div>
      );
};

Modal.propTypes = {
    show: PropTypes.bool.isRequired,
    onClose: PropTypes.func.isRequired,
    title: PropTypes.string,
    children: PropTypes.node.isRequired,
};

export default Modal;
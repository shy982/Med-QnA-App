import React from 'react';

const Navbar = () => {
  return (
    <div className="flex h-[80px] sm:h-[90px] border-b border-neutral-300 py-4 px-4 sm:px-8 items-center relative">
      <iframe
        src="https://lottie.host/embed/bfc1d7b9-e48d-479d-9ee7-a24ffdf90d8c/9RlwH5J5lq.json"
        width="60" 
        height="60"
        allowFullScreen
        className="absolute left-4 top-1/2 transform -translate-y-1/2"
      ></iframe>

      <div className="font-bold text-4xl flex items-center ml-8">
        <a
          className="hover:opacity-50"
          href="#"
        >
          &nbsp; MediMate
        </a>
      </div>
    </div>
  );
};

export default Navbar;

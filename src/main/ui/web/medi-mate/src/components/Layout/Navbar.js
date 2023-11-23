import React from 'react';

const Navbar = () => {
  return (
    <div className="flex h-[50px] sm:h-[60px] border-b border-neutral-300 py-2 px-2 sm:px-8 items-center justify-between">
      <div className="font-bold text-3xl flex items-center">
        <a
          className="ml-2 hover:opacity-50"
          href=""
        >
          Medical Q&A App
        </a>
      </div>
    </div>
  );
};

export default Navbar;

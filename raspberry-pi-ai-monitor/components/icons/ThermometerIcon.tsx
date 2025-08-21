
import React from 'react';

export const ThermometerIcon: React.FC<React.SVGProps<SVGSVGElement>> = (props) => (
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" {...props}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.375v11.25m-3.75-8.25h7.5" />
        <path strokeLinecap="round" strokeLinejoin="round" d="M12 21a8.25 8.25 0 0 1-8.25-8.25V9a8.25 8.25 0 0 1 16.5 0v3.75A8.25 8.25 0 0 1 12 21Z" />
    </svg>
);

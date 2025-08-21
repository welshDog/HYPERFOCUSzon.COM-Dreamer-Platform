
import React from 'react';

export const CpuIcon: React.FC<React.SVGProps<SVGSVGElement>> = (props) => (
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" {...props}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 21v-1.5M15.75 3v1.5M15.75 21v-1.5M3.75 15.75H21m-17.25-9H21" />
        <path strokeLinecap="round" strokeLinejoin="round" d="M9 7.5h6m-6 3h6m-6 3h6m3-9h.008v.008H18V7.5Zm-12 0h.008v.008H6V7.5Zm12 3h.008v.008H18v-.008Zm-12 0h.008v.008H6v-.008Zm12 3h.008v.008H18v-.008Zm-12 0h.008v.008H6v-.008Z" />
    </svg>
);

import React, { Suspense, useState, useEffect, ReactNode, lazy } from 'react';
// Check if file exists and dynamically load it

const loadComponent = (componentPath: string) => {
  return lazy(() => import(`${componentPath}`));
};
const DynamicComponent = loadComponent('../components/Dynamic.tsx');
const App = () => {

  return (
    <div>
      <h1>Dynamic Frontend Component</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <DynamicComponent />
      </Suspense></div>
  );
};

export default App;

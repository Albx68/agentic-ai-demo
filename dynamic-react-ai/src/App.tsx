import React, { Suspense, useState, useEffect, ReactNode } from 'react';

// Check if file exists and dynamically load it
const loadComponent = async (componentPath: string) => {
  try {
    // Dynamically import the component file
    const component = await import(`${componentPath}`);
    return component;
  } catch (error) {
    console.error(`Error loading component from ${componentPath}:`, error);
    return null;
  }
};

const App = () => {
  const [isComponentReady, setIsComponentReady] = useState(false);
  const [Component, setComponent] = useState<ReactNode>(() => <></>);

  useEffect(() => {
    const checkAndLoadComponent = async () => {
      const componentPath = './components/ChatUI'; // Adjust path as needed

      const importedComponent = await loadComponent(componentPath);

      if (importedComponent) {
        setComponent(importedComponent.default);
        setIsComponentReady(true);
      }
    };

    checkAndLoadComponent();
  }, []);

  return (
    <div>
      <h1>Dynamic Frontend Component</h1>
      {isComponentReady ? (
        <Suspense fallback={<div>Loading...</div>}>
          <Component />
        </Suspense>
      ) : (
        <p>Component not yet available. Please check if the file exists and is generated.</p>
      )}
    </div>
  );
};

export default App;

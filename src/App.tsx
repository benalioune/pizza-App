import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline, AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import Menu from './components/Menu';
import Login from './components/Login';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

const App: React.FC = () => {
  const isAuthenticated = !!localStorage.getItem('token');

  const handleLogout = () => {
    localStorage.removeItem('token');
    window.location.href = '/login';
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Box sx={{ flexGrow: 1 }}>
          <AppBar position="static">
            <Toolbar>
              <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                Pizza Restaurant
              </Typography>
              {isAuthenticated && (
                <Button color="inherit" onClick={handleLogout}>
                  Logout
                </Button>
              )}
            </Toolbar>
          </AppBar>

          <Routes>
            <Route
              path="/login"
              element={isAuthenticated ? <Navigate to="/menu" /> : <Login />}
            />
            <Route
              path="/menu"
              element={isAuthenticated ? <Menu /> : <Navigate to="/login" />}
            />
            <Route
              path="/"
              element={<Navigate to={isAuthenticated ? "/menu" : "/login"} />}
            />
          </Routes>
        </Box>
      </Router>
    </ThemeProvider>
  );
};

export default App; 
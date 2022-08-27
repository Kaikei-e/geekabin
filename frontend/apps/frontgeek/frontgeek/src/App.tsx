import type { Component } from 'solid-js';

import logo from './logo.svg';
import styles from './App.module.css';
import {Box} from "@suid/material/Box";
import TextField from "@suid/material/TextField";

const App: Component = () => {
  return (
    <div class={styles.App}>
      <Box width={'100%'} minWidth={'100vw'}
           height={'100%'} minHeight={'100vh'}
           backgroundColor={'skyblue'}
           padding={'5px'}
           flexDirection={'column'}
           alignItems={'flex-start'}
      >
          <Box width={'100%'} height={'100%'} textAlign={'start'}>
              <text font-size={'20px'} color={'white'}>Geekabin</text>

          </Box>
      </Box>
    </div>
  );
};

export default App;

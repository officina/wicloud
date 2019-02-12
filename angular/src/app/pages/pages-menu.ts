import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Dashboard',
    icon: 'nb-home',
    link: '/pages/dashboard',
    home: true,
  },
  {
    title: 'Your things',
    group: true,
  },
  {
    title: 'Auth',
    icon: 'nb-locked',
    children: [
      {
        title: 'Login',
        link: '/auth/login',
      },
      {
        title: 'Register',
        link: '/auth/register',
      },
      {
        title: 'Request Password',
        link: '/auth/request-password',
      },
      {
        title: 'Reset Password',
        link: '/auth/reset-password',
      },
    ],
  },
  {
    title: 'Installations',
    link: '/pages/installation-wilamp',
    icon: 'nb-tables',
  },
    {
    title: 'Nodes',
    link: '/pages/node-wilamp',
    icon: 'nb-tables',
  },
    {
    title: 'Gateways',
    link: '/pages/gateway-wilamp',
    icon: 'nb-tables',
  },
];

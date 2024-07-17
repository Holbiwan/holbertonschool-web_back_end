export default [
    {
      files: ['**/*.js'],
      languageOptions: {
        ecmaVersion: 2021,
        sourceType: 'module',
      },
      rules: {
        'no-console': 'off',
        'indent': ['error', 2],
      },
      extends: [
        'eslint:recommended',
        'airbnb-base',
      ],
      env: {
        browser: true,
        es2021: true,
        node: true,
      },
    },
  ];
  
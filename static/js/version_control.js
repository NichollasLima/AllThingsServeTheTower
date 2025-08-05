    const timestamp = new Date().getTime();
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = `styles.css?v=${timestamp}`;
    document.head.appendChild(link);

    const script = document.createElement('script');
    script.src = `app.js?v=${timestamp}`;
    document.body.appendChild(script);
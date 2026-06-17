const useDataLoading = (url) => {
    useEffect(() => {
        const abortController = new AbortController

        fetch(url, {signal: abortController.signal})
        .then((response) => response.json())
        .then((data) => {setData(data); setIsLoading(false) });

        return () => {
            abortController.abort();
        };
}, []);

return{ data, error, isLoading }
}
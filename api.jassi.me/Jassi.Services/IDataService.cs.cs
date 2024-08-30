namespace Jassi.Services
{
    public interface IDataService
    {
        Task<IEnumerable<T>> GetAllAsync<T>(string query);
        Task ExecuteAsync(string query);
    }
}


const Container = ({ children }) => {
    return (
        <div className="h-screen bg-img bg-slate-950 bg-opacity-50 bg-blend-overlay bg-cover bg-center bg-no-repeat flex justify-between">
            {children}
        </div>
    )
}

export default Container
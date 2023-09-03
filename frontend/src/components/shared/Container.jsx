
const Container = ({ children }) => {
    return (
        <div className="h-screen bg-img bg-cover bg-center bg-no-repeat flex justify-between">
            {children}
        </div>
    )
}

export default Container